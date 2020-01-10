from app.common.constant import SystemResourceList


class Permission:
    manage_permission = {
        700100,
        700200,
        700102,
        700300
    }
    tyfo_permission = SystemResourceList.permission_web.keys() - manage_permission

    yn_permission = SystemResourceList.permission_yn_web.keys()

    permission_type = {
        'tyfo': 1,
        'yn': 2,
        'manage': 3
    }
