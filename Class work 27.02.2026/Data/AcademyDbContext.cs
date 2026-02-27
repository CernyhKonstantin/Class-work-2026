using Microsoft.EntityFrameworkCore;
using Academy.Entities;

public class AcademyDbContext : DbContext
{
    public AcademyDbContext(DbContextOptions<AcademyDbContext> options)
        : base(options)
    {
    }

    public DbSet<Student> Students { get; set; }
    public DbSet<Group> Groups { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Rename table
        modelBuilder.Entity<Student>().ToTable("Users");

        // Default value
        modelBuilder.Entity<Student>()
            .Property(s => s.Name)
            .HasDefaultValue("No Name");

        // One Group -> Many Students
        modelBuilder.Entity<Group>()
            .HasMany(g => g.Students)
            .WithOne(s => s.Group)
            .HasForeignKey(s => s.GroupId)
            .OnDelete(DeleteBehavior.Cascade);

        base.OnModelCreating(modelBuilder);
    }
}