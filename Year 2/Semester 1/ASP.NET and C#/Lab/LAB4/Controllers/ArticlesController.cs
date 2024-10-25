using LAB4.Models;
using Microsoft.AspNetCore.Mvc;

namespace LAB4.Controllers
{
    public class ArticlesController : Controller
    {
        [NonAction]
        public Article[] GetArticles()
        {
            // Se instantiaza un array de articole
            Article[] articles = new Article[3];
            // Se creeaza articolele
            for (int i = 0; i < 3; i++)
            {
                Article article = new Article();
                article.Id = i;
                article.Title = "Articol " + (i + 1).ToString();
                article.Content = "Continut articol " + (i + 1).ToString();
                article.Date = DateTime.Now;
                // Se adauga articolul in array
                articles[i] = article;
            }
            return articles;
        }

        // Afisarea tuturor articolelor
        // Pentru afisare utilizam GET
        // Intotdeauna se executa implicit HttpGet
        public IActionResult Index()
        {
            Article[] art = GetArticles();
            ViewBag.Articole = art;
            return View();
        }

        // Implicit GET: Afisarea unui singur articol
        public IActionResult Show(int? id)
        {
            Article[] articles = GetArticles();
            try
            {
                ViewBag.Article = articles[(int)id];
                return View();
            } 
            catch(Exception ex)
            {
                //return StatusCode(StatusCodes.Status404NotFound);
                ViewBag.ErrorMessage = ex.Message;
            }

            return View();
        }

        [HttpGet]
        public IActionResult New()
        {
            return View();
        }

        [HttpPost]
        public IActionResult New(Article article)
        {
            // ... cod creare articol ...
            return View("NewPostMethod");
        }
    }
}
