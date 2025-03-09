def user_context(request):
    print(f"Context processor: user={request.user}")  # Log de depuração
    return {
        "user": request.user,
    }
