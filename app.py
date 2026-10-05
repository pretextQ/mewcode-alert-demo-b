def owner_name(user):
    profile = user.get('profile') or {}
    return (profile.get('name') or '').upper()
