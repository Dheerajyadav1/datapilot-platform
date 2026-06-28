-- ============================================================================
-- File: 03_roles.sql
-- Purpose: Create read-only user for AI-generated SQL queries
-- ============================================================================

-- Create read-only role
DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT
        FROM pg_catalog.pg_roles
        WHERE rolname = 'readonly_user'
    ) THEN
        CREATE ROLE readonly_user
        LOGIN
        PASSWORD 'readonly_password';
    END IF;
END
$$;

-- Allow database connection
GRANT CONNECT ON DATABASE agentic_db TO readonly_user;

-- Allow schema access
GRANT USAGE ON SCHEMA raw TO readonly_user;
GRANT USAGE ON SCHEMA staging TO readonly_user;
GRANT USAGE ON SCHEMA marts TO readonly_user;
GRANT USAGE ON SCHEMA embeddings TO readonly_user;

-- Read access to existing tables
GRANT SELECT ON ALL TABLES IN SCHEMA raw TO readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA staging TO readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA marts TO readonly_user;
GRANT SELECT ON ALL TABLES IN SCHEMA embeddings TO readonly_user;

-- Read access to future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA raw
GRANT SELECT ON TABLES TO readonly_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA staging
GRANT SELECT ON TABLES TO readonly_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA marts
GRANT SELECT ON TABLES TO readonly_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA embeddings
GRANT SELECT ON TABLES TO readonly_user;