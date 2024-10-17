using Microsoft.AspNetCore.Mvc;

namespace LAB3.Controllers
{
    public class StudentsController : Controller
    {
        public string Index()
        {
            return "Afisare lista studenti";
        }

        public string Show(int? id)
        {
            if (id == null)
            {
                return "Introduceti un id";
            }

            return "Afisare student cu id: " + id;
        }

        public string Create()
        {
            return "Creare student in baza de date";
        }

        public string Edit(int? id)
        {
            if (id == null)
            {
                return "Introduceti un id";
            }

            return "Editare student cu id: " + id;
        }

        public string Delete(int? id)
        {
            if (id == null)
            {
                return "Introduceti un id";
            }

            return "Delete student cu id: " + id;
        }
    }
}
