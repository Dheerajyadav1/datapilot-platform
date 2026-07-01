class Formatter:

    @staticmethod
    def currency(value):

        if value is None:
            return "$0.00"
        return f"${value:,.2f}"

    @staticmethod
    def integer(value):

        if value is None:
            return "0"
        return f"{value:,}"

    @staticmethod
    def percentage(value):

        if value is None:
            return "0.00%"
        return f"{value:.2f}%"

    @staticmethod
    def millions(value):

        if value is None:
            return "$0.00 M"
        return f"${value/1_000_000:.2f} M"

    @staticmethod
    def thousands(value):

        if value is None:
            return "0.0 K"
        return f"{value/1000:.1f} K"
