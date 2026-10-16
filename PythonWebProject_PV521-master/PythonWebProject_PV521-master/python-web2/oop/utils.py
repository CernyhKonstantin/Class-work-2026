from datetime import datetime

def current_timestamp()->str:
    return str(
        int(
            datetime.timestamp(
                datetime.now()
            )
        )
    )