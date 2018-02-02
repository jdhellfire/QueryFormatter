class QueryFormatter(object):
    def translate(self, quer_str):
        return quer_str.lower().replace('-', '\\-')
