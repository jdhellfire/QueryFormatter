class QueryFormatter(object):
    def translate(self, quer_str):
        return quer_str.lower() if quer_str.startswith("\"") and quer_str.endswith("\"") \
                                else quer_str.lower().replace('-', '\\-')
