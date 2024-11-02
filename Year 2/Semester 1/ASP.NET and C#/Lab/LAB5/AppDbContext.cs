using Microsoft.EntityFrameworkCore;

namespace Lab5.Models
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

        public DbSet<Article> Articles { get; set; }

        public DbSet<Category> Categories { get; set; }

    }
}
