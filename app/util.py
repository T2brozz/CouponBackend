from shortuuid import ShortUUID


def uuid(length: int = 8) -> str:
    return str(ShortUUID().random(length=length))
