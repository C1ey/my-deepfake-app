from workers import Response

async def on_fetch(request):
    if request.method == "POST":
        # Placeholder: Accept file upload, do analysis here
        return Response.json({"message": "Deepfake analysis placeholder!"})
    return Response.json({"message": "Send a POST request with a file."})
