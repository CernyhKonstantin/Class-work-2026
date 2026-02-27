using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace Academy.Entities;

public class Student
{
    public int Id { get; set; }
    public int StudentNumber { get; set; }

    public string Name { get; set; } = string.Empty;
    public string Surname { get; set; } = string.Empty;

    public int GroupId { get; set; }
    public Group Group { get; set; } = null!;

    public DateTime? CreatedAt { get; set; }
}
