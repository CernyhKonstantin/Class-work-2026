using Academy.Context;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;

internal class Program
{
    static void Main(string[] args)
    {
        var services = new ServiceCollection();

        var configuration = new ConfigurationBuilder()
            .SetBasePath(Directory.GetCurrentDirectory())
            .AddJsonFile("appsettings.json")
            .Build();

        services.AddDbContext<AcademyDbContext>(options =>
            options.UseSqlServer(
                configuration.GetConnectionString("MSSQLConnection")));

        var provider = services.BuildServiceProvider();

        using var scope = provider.CreateScope();
        var context = scope.ServiceProvider.GetRequiredService<AcademyDbContext>();

        if (context.Database.CanConnect())
        {
            Console.WriteLine("Connection to the database is established.");
        }
        else
        {
            Console.WriteLine("Failed to connect to the database.");
        }
    }
}