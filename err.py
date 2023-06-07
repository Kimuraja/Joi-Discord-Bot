from discord.ext.commands import CommandError


class MemberNotFoundError(CommandError):
    def __init__(self, argument):
        self.argument = argument
        super().__init__(f"Member '{argument}' not found")


class MissingPermissionsError(CommandError):
    def __init__(self, permissions):
        self.permissions = permissions
        super().__init__(f"Missing permissions: {permissions}")


class InvalidRoleError(CommandError):
    def __init__(self, role):
        self.role = role
        super().__init__(f"Invalid role: {role}")
