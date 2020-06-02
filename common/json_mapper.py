import json


class JsonMapper:
    """
    This class will be helpful in performing
    JSON related operations
    """

    def __init__(self):
        pass

    def serialize_json_key_values(self, dict, keys):
        """
        This method will be helpul in converting
        values which are in dict object type to str
        JSON format for specified keys
        :param dict: expects the dictonary to be serialized
        :param keys: expects set of keys to be serialized
        :return: dictonary of serialized keys
        """
        for key in keys:
            dict[key] = json.dumps(dict[key])
        return dict

    def deserialize_json_key_values(self, dict, keys):
        """
        This method will be helpul in converting
        values which are in dict string type to object
        JSON format for specified keys
        :param dict: expects the dictonary to be deserialized
        :param keys: expects set of keys to be deserialized
        :return: dictonary of deserialized keys
        """
        for key in keys:
            dict[key] = json.loads(dict[key])
        return dict
