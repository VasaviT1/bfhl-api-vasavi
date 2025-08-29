@echo off
echo Testing BFHL API with curl...
echo Make sure to run: python main.py first
echo.

echo Example A:
curl -X POST http://localhost:5000/bfhl -H "Content-Type: application/json" -d "{\"data\": [\"a\",\"1\",\"334\",\"4\",\"R\",\"$\"]}"
echo.
echo.

echo Example B:
curl -X POST http://localhost:5000/bfhl -H "Content-Type: application/json" -d "{\"data\": [\"2\",\"a\",\"y\",\"4\",\"&\",\"-\",\"*\",\"5\",\"92\",\"b\"]}"
echo.
echo.

echo Example C:
curl -X POST http://localhost:5000/bfhl -H "Content-Type: application/json" -d "{\"data\": [\"A\",\"ABcD\",\"DOE\"]}"
echo.
echo.

echo GET endpoint test:
curl -X GET http://localhost:5000/bfhl
echo.