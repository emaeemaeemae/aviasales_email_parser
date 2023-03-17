class BaseError(Exception):
    pass


class GetEmailListError(BaseError):
    pass


class EmailListDecodeError(BaseError):
    pass


class GetEmailHeaderError(BaseError):
    pass


class EmailMessageDecodeError(BaseError):
    pass


class GetCityError(BaseError):
    pass


class GetPriceError(BaseError):
    pass
