class SparrowAPIError(Exception):
    """
    An exception raised in case of non-success response from Sparrow.
    """
    def __init__(self, data):
        super(SparrowAPIError, self).__init__(data.get("textresponse", repr(data)))
        self.data = data
