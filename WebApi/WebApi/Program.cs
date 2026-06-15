using WebApi.Models;

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

List<Product> products = new List<Product>();

app.MapGet("/", () => "WebApi is running successfully!");

app.MapGet("/product", () =>
{
    return products.Where(p => p.IsActive);
});

app.MapGet("/product/{id:int}", (int id) =>
{
    var product = products.FirstOrDefault(p => p.Id == id);

    if (product == null)
    {
        return Results.NotFound();
    }

    return Results.Ok(product);
});

app.MapPost("/product", (Product product) =>
{
    bool exists = products.Any(p =>
        p.Title.Equals(product.Title, StringComparison.OrdinalIgnoreCase));

    if (exists)
    {
        return Results.BadRequest("A product with this title already exists.");
    }

    products.Add(product);

    return Results.Created($"/product/{product.Id}", product);
});

app.MapPut("/product/{id:int}", (int id, Product updatedProduct) =>
{
    var product = products.FirstOrDefault(p => p.Id == id);

    if (product == null)
    {
        return Results.NotFound();
    }

    product.Title = updatedProduct.Title;
    product.Price = updatedProduct.Price;
    product.Count = updatedProduct.Count;
    product.Discount = updatedProduct.Discount;
    product.IsActive = updatedProduct.IsActive;

    return Results.Ok(product);
});

app.MapDelete("/product/{id:int}", (int id) =>
{
    var product = products.FirstOrDefault(p => p.Id == id);

    if (product == null)
    {
        return Results.NotFound();
    }

    products.Remove(product);

    return Results.Ok(product);
});

app.Run();