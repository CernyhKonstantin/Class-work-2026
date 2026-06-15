namespace WebApi.Models;

public class Product
{
    private static int _nextId = 1;

    public Product()
    {
        Id = _nextId++;
    }

    public int Id { get; private set; }

    public string Title { get; set; } = string.Empty;

    public decimal Price { get; set; }

    public int Count { get; set; }

    public double Discount { get; set; }

    public bool IsActive { get; set; }
}