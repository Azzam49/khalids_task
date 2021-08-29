# Class to build a json object
class JsonUtils:

    @staticmethod
    def json_object(model_name, actual_count, data, errmsg=""):
        obj = {
            model_name: {
                "actual_count": actual_count,
                "data": data
            },
            "errMsg": errmsg
        }
        return obj