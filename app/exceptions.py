from fastapi import Depends, HTTPException, status

privlige_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="User is not admin",
    headers={"WWW-Authenticate": "Bearer"},
)

credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

not_found_exception = HTTPException(
        status_code=404,
        detail="Unable to find resource",
        headers={"WWW-Authenticate": "Bearer"},
    )