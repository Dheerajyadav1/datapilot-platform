import os
import sys

# Force project root to be resolved first to avoid library namespace conflicts
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, root_dir)

import streamlit as st
import pandas as pd

import agents
from agents.core.context import AgentContext
from agents.core.orchestrator import AgentOrchestrator

from app.components.sidebar import Sidebar
from app.components.footer import Footer
from app.utils.helpers import load_css, render_header

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
)

load_css()
Sidebar.render()

render_header("AI Data Assistant", "Ask questions about your data warehouse, pipeline health, business trends, or platform architecture.")
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        # If there is cached structured data in the message, render it!
        if "sql" in message and message["sql"]:
            with st.expander("Generated SQL"):
                st.code(message["sql"], language="sql")
                
        if "df" in message and message["df"] is not None:
            with st.expander("Query Result"):
                st.dataframe(message["df"], use_container_width=True)
                
        if "insights" in message and message["insights"]:
            with st.expander("Insights"):
                for insight in message["insights"]:
                    st.write(f"• {insight}")
                    
        if "recommendations" in message and message["recommendations"]:
            with st.expander("Recommendations"):
                for rec in message["recommendations"]:
                    st.write(f"• {rec}")
                    
        if "docs" in message and message["docs"]:
            with st.expander("Retrieved Documents"):
                for idx, doc in enumerate(message["docs"], start=1):
                    st.markdown(f"### Document {idx}")
                    st.write(doc)
                    
        if "trace" in message and message["trace"]:
            with st.expander("Execution Trace"):
                for step in message["trace"]:
                    st.write(step)
                    
        if "tools" in message and message["tools"]:
            with st.expander("Tools Used"):
                st.write(", ".join(message["tools"]))

question = st.chat_input("Ask anything...")

if question:
    # Append user question
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )
    with st.chat_message("user"):
        st.markdown(question)

    with st.spinner("Thinking..."):
        try:
            # Build agent execution context
            context = AgentContext(
                question=question
            )
            
            # Load conversation history from session state
            for m in st.session_state.messages[:-1]:
                context.conversation_history.append({
                    "role": m["role"],
                    "content": m["content"]
                })

            orchestrator = AgentOrchestrator()
            context = orchestrator.execute(context)
            
            # Extract main response
            assistant_response = context.response if context.response else "Here is the result of your query."

            # Construct message with extra visualization components cached
            assistant_msg = {
                "role": "assistant",
                "content": assistant_response,
                "sql": context.generated_sql,
                "df": context.dataframe,
                "insights": context.insights,
                "recommendations": context.recommendations,
                "docs": context.retrieved_documents,
                "trace": context.execution_trace,
                "tools": context.tools_used,
            }

            st.session_state.messages.append(assistant_msg)

            # Render response
            with st.chat_message("assistant"):
                st.markdown(assistant_response)

                if context.generated_sql:
                    with st.expander("Generated SQL"):
                        st.code(context.generated_sql, language="sql")

                if context.dataframe is not None:
                    with st.expander("Query Result"):
                        st.dataframe(context.dataframe, use_container_width=True)

                if context.insights:
                    with st.expander("Insights"):
                        for insight in context.insights:
                            st.write(f"• {insight}")

                if context.recommendations:
                    with st.expander("Recommendations"):
                        for recommendation in context.recommendations:
                            st.write(f"• {recommendation}")

                if context.retrieved_documents:
                    with st.expander("Retrieved Documents"):
                        for index, document in enumerate(context.retrieved_documents, start=1):
                            st.markdown(f"### Document {index}")
                            st.write(document)

                if context.execution_trace:
                    with st.expander("Execution Trace"):
                        for step in context.execution_trace:
                            st.write(step)

                if context.tools_used:
                    with st.expander("Tools Used"):
                        st.write(", ".join(context.tools_used))

                st.caption(
                    f"Execution Time: {context.execution_time:.2f} sec"
                )
        except Exception as e:
            error_response = f"An error occurred while executing the request: {e}"
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_response
            })
            with st.chat_message("assistant"):
                st.error(error_response)

Footer.render()
