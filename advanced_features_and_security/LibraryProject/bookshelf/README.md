# Permissions and Groups Setup

## Groups:
- Editors: can_view, can_create, can_edit
- Viewers: can_view
- Admins: can_view, can_create, can_edit, can_delete

## Usage in Views:
- Use @permission_required('bookshelf.permission_codename', raise_exception=True)
- Ensure users belong to the appropriate group to access features
