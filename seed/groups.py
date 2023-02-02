from database.db import session
from database.models import Sgroup


def create_groups():
    for name in range(1, 4):
        group = Sgroup(
            group_name=f"group {name}"
        )
        # print(f"{group.group_name}")
        session.add(group)
    session.commit()


if __name__ == '__main__':
    create_groups()
