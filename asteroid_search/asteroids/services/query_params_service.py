class QueryParamsService(object):
    '''
    Pepare request information to serializer and query'''
    def get_object_params(self, query_params):
        query_array = query_params.split('&')
        params = {}
        for param in query_array:
            split_param = param.split('=')
            params[split_param[0]] = int(split_param[1])
        return params