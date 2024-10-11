using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LAB2
{
    public class Employee
    {
        public int EmployeeId { get; set; }
        public string? FirstName { get; set; }
        public string? LastName { get; set; }
        public string Salary { get; set; }

        public Employee(int employeeId, string? firstName, string? lastName, string salary)
        {
            this.EmployeeId = employeeId;
            this.FirstName = firstName;
            this.LastName = lastName;
            this.Salary = salary;
        }

        public void Print()
        {
            Console.WriteLine($"Employee ID: {this.EmployeeId}");
            Console.WriteLine($"First name: {this.FirstName}");
            Console.WriteLine($"Last name: {this.LastName}");
            Console.WriteLine($"Salary: {this.Salary}\n");
        }
    }
}
