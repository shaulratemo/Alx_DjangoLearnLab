### Authentication & Permissions
- Authentication: Token-based (obtain via POST `/api/auth/token/` with username & password).
- Authorization:
  - Default: `IsAuthenticated` → all endpoints require login.
  - BookViewSet: Uses `IsAdminOrReadOnly` → only staff can create/update/delete, others can read.
- Usage: Send token in headers → `Authorization: Token <your_token>`.