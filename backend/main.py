from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware



# ============================================================
# 1. FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="ChitrAI API",
    description="Generative AI Image Studio",
    version="1.0.0",

    # Default FastAPI Swagger Docs ko disable kar rahe hain
    # kyunki humein apna custom branded /docs page banana hai.
    docs_url=None
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from image_routes import router as image_router
app.include_router(image_router)

# ============================================================
# 2. STATIC FILES
# ============================================================

# static folder ke andar rakhi images/files ko browser se access
# karne ke liye serve kar rahe hain.
#
# Example:
# static/chitrai-logo.png
#
# Browser URL:
# http://127.0.0.1:8000/static/chitrai-logo.png

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# ============================================================
# 3. CUSTOM SWAGGER DOCS
# ============================================================

@app.get("/docs", include_in_schema=False)
async def custom_docs():

    return HTMLResponse("""
    <!DOCTYPE html>

    <html>

    <head>

        <!-- Browser TAB ka title -->
        <title>ChitrAI API Docs</title>


        <!-- =================================================
             FAVICON
             =================================================

             Ye browser TAB ke andar chhota ChitrAI logo
             dikhane ke liye hai.

             Same PNG use kar rahe hain:
             /static/chitrai-logo.png
        -->

        <link
            rel="icon"
            type="image/png"
            href="/static/chitrai-logo.png"
        >


        <!-- =================================================
             SWAGGER UI CSS
             =================================================

             Swagger UI ka official styling load kar raha hai.
        -->

        <link
            rel="stylesheet"
            href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css"
        >


        <!-- =================================================
             CUSTOM CHITRAI HEADER CSS
             =================================================

             Ye Swagger page ke TOP par hamara logo
             dikhane ke liye hai.
        -->

        <style>

            body {
                margin: 0;
                background: #ffffff;
            }

            .chitrai-header {

                height: 90px;

                display: flex;

                align-items: center;

                justify-content: center;

                background: #ffffff;

                border-bottom: 1px solid #eeeeee;
            }


            /* TOP PAR CHITRAI LOGO */

            .chitrai-header img {

                height: 55px;

                width: auto;

                object-fit: contain;
            }

        </style>

    </head>


    <body>


        <!-- =================================================
             CHITRAI LOGO - SWAGGER PAGE
             =================================================

             Ye favicon nahi hai.

             Ye actual Swagger page ke TOP par
             bada logo show karega.
        -->

        <div class="chitrai-header">

            <img
                src="/static/chitrai-logo.png"
                alt="ChitrAI Logo"
            >

        </div>


        <!-- =================================================
             SWAGGER UI CONTAINER
             =================================================

             Swagger ka complete API documentation
             yahan render hoga.
        -->

        <div id="swagger-ui"></div>


        <!-- =================================================
             SWAGGER UI JAVASCRIPT
             =================================================

             Swagger UI ko browser mein initialize karta hai.
        -->

        <script
            src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js">
        </script>


        <script>

            window.onload = function() {

                SwaggerUIBundle({

                    /*
                     * FastAPI automatically OpenAPI JSON
                     * generate karta hai.
                     *
                     * Is JSON mein tumhare saare API endpoints
                     * ki information hoti hai.
                     */

                    url: "/openapi.json",


                    /*
                     * Swagger ko is HTML element ke andar
                     * render karna hai.
                     */

                    dom_id: "#swagger-ui",


                    /*
                     * Swagger ke API presets.
                     */

                    presets: [
                        SwaggerUIBundle.presets.apis
                    ],


                    /*
                     * Swagger ka basic layout.
                     */

                    layout: "BaseLayout"

                });

            };

        </script>


    </body>

    </html>
    """)


# ============================================================
# 4. TEST / HEALTH ENDPOINT
# ============================================================

@app.get("/health")
def health():

    return {
        "status": "OK",
        "message": "ChitrAI Backend Running"
    }