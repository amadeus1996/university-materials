using Microsoft.AspNetCore.Mvc;

namespace LAB3.Controllers
{
    public class ExamplesController : Controller
    {
        public string Concatenare(string? s1, string? s2)
        {
            return s1 + " " + s2;
        }

        public string Produs(int param1, int? param2)
        {
            if (param2 == null)
                return "Introduceti parametrul 2";
            return (param1 * param2).ToString();
        }

        public string Operatie(int? param1, int? param2, string? param3)
        {
            if (param1 == null || param1 is not int)
                return "Introduceti parametrul 1";
            if (param2 == null || param2 is not int)
                return "Introduceti parametrul 2";
            if (param3 == null)
                return "Introduceti parametrul 3";

            int? aux;
            if (param3 == "plus")
                aux = param1 + param2;
            else if (param3 == "minus")
                aux = param1 - param2;
            else if (param3 == "ori")
                aux = param1 * param2;
            else if (param3 == "div")
                aux = param1 / param2;
            else return "Operator invalid pentru parametrul 3";

            return param1.ToString() + " " + param3 + " " + param2.ToString() + " = " + aux.ToString();
        }
    }
}
