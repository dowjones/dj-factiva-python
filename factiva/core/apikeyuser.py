
class APIKeyUser:
    """
    Class that represents an API user. This entity is identifiable by an API-Key.
    Parameters
    ----------
    api_key : string that contains the 32-character long APi Key
    See Also
    --------
    UserOAuth: API user that follows the OAuth guidelines.
    Examples
    --------
    Creating a new API user.
    >>> ua = UserAPI('abcdefghabcdefghabcdefghabcdefgh')
    >>> ua
        {
            "key": "abcdefghabcdefghabcdefghabcdefgh",
            "cnt_curr_ext": 0,
            "current_downloaded_amount": 0,
            "max_allowed_concurrent_extracts": 1,
            "max_allowed_document_extracts": 2500000,
            "max_allowed_extracts": 5,
            "name": "Account Name",
            "products": "DNA",
            "tot_document_extracts": 0,
            "tot_extracts": 0,
            "tot_subscriptions": 0,
            "tot_topics": 0
        }
    """

    _DJ_API_HOST = 'https://api.dowjones.com'
    _DJ_API_ACCOUNT_PATH = '/alpha/accounts'

    def __init__(
        self,
        api_key=None,
        get_info=True
    ):
        if api_key is None:
            raise ValueError('Factiva API-Key value does not exist')

        if len(api_key) != 32:
            raise ValueError('Factiva API-Key has the wrong length')

        self.api_key = api_key
        
        if get_info is True:
            self._account_endpoint = f'{self._DJ_API_HOST}{self._DJ_API_ACCOUNT_PATH}/{self.api_key}'
        else:
            self._account_endpoint = None
