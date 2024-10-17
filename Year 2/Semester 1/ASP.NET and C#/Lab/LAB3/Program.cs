var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();


// ... concatenare/param/param
/*
app.MapControllerRoute(
    name: "",
    pattern: "concatenare/{controller=Examples}/{action=Concatenare}/{s1}/{s2}"
    );
*/

// EX 1
app.MapControllerRoute(
    name: "Concatenare",
    pattern: "concatenare/{s1?}/{s2?}",
    defaults: new { controller = "Examples", action = "Concatenare" });

// EX 2
app.MapControllerRoute(
    name: "Produs",
    pattern: "produs/{param1}/{param2?}",
    defaults: new { controller = "Examples", action = "Produs" });

// EX 3
app.MapControllerRoute(
    name: "Operatie",
    pattern: "operatie/{param1?}/{param2?}/{param3?}",
    defaults: new { controller = "Examples", action = "Operatie" });

// EX 4
app.MapControllerRoute(
    name: "StudentsAll",
    pattern: "students/all",
    defaults: new { controller = "Students", action = "Index"});

app.MapControllerRoute(
    name: "StudentCreate",
    pattern: "students/new",
    defaults: new { controller = "Students", action = "Create"});

app.MapControllerRoute(
    name: "StudentShow",
    pattern: "students/show/{id?}",
    defaults: new { controller = "Students", action = "Show" });

app.MapControllerRoute(
    name: "StudentEdit",
    pattern: "students/edit/{id?}",
    defaults: new { controller = "Students", action = "Edit"});

app.MapControllerRoute(
    name: "StudentDelete",
    pattern: "students/delete/{id?}",
    defaults: new { controller = "Students", action = "Delete"});

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
