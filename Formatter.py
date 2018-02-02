class QueryFormatter(object):
    def translate(self, quer_str):
        if quer_str.startswith("\"") and quer_str.endswith("\""):
            return quer_str.lower()
        return quer_str.lower().replace('-', '\\-')

