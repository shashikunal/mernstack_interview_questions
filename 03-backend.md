# 03 - Backend: Node.js + Express OR .NET

Choose track per job desc. Learn one deeply, other at overview level.

## A. Node.js + Express - Top 20

1. **Node event loop + non-blocking?**
   Single-thread + libuv threadpool for I/O. Don't block with sync/crypto loops - use worker threads/queues.
2. **Middleware chain?**
   `(req,res,next)=>{...; next()}`. Order matters. `app.use(express.json())` first, routes, then error handler with 4 args.
3. **Global error handling?**
   `app.use((err,req,res,next)=>res.status(err.status||500).json({message:err.message}))` + async wrapper: `const ah=fn=>(r,s,n)=>Promise.resolve(fn(r,s,n)).catch(n)`.
4. **JWT auth flow?**
   Login -> sign access(15m)+refresh(7d) -> client sends `Authorization: Bearer` -> `verify()` middleware attaches `req.user`. Refresh rotates. Logout blacklists/invalidate.
5. **Where store tokens?**
   Access in memory, refresh in HttpOnly SameSite cookie. Never localStorage for sensitive (XSS).
6. **Hash passwords?**
   `bcrypt.hash(pw,12)` + `bcrypt.compare`. Never plain/MD5. Add salt rounds.
7. **Validation?**
   zod/express-validator/Joi at boundary. Return 400 with details. Never trust client.
8. **REST design?**
   `GET /users/:id`, `POST /users`, `PUT` replace, `PATCH` partial, `DELETE`. Status: 200/201/204/400/401/403/404/409/429/500. Version `/api/v1`.
9. **AuthZ: RBAC?**
   Middleware `requireRole('admin')` checks `req.user.role`. 401 unauthenticated, 403 unauthorized.
10. **Rate limit + security headers?**
    `express-rate-limit`, `helmet`, `cors({origin:allowlist})`, sanitize input.
11. **File upload?**
    Multer/S3 presigned URLs. Limit size/type, scan, store outside webroot.
12. **Pagination?**
    Cursor (`?cursor=&limit=`) for large/infinite, offset (`?page=&limit=`) for admin. Always cap limit + return total.
13. **N+1 + caching?**
    Batch with DataLoader, cache with Redis `GET cache || DB+SETEX`. Invalidate on write.
14. **Transactions?**
    Mongo sessions / Postgres `BEGIN/COMMIT`. For money/stock ops.
15. **Logging + health?**
    pino/winston JSON logs + `/health` + graceful shutdown `process.on('SIGTERM')`.
16. **Cluster/PM2?**
    `cluster` fork per CPU, PM2 manages. Stateless app + sticky not needed if JWT.
17. **Testing?**
    Supertest + vitest/jest: `request(app).post('/login').send(...)` expect 200.
18. **Env config?**
    dotenv + validate required vars on boot, never commit `.env`.
19. **WebSocket vs SSE?**
    WS bidirectional (chat), SSE one-way server push (feed). REST for CRUD.
20. **Design CRUD in 5 min?**
    Router->Controller->Service->Model, DTO validation, error middleware. Say aloud.

Snippet to memorize:
```js
function auth(req,res,next){
 const h=req.headers.authorization;
 if(!h?.startsWith('Bearer ')) return res.status(401).json({message:'No token'});
 try{ req.user=jwt.verify(h.slice(7),process.env.JWT_SECRET); next();}
 catch{ return res.status(401).json({message:'Invalid token'});}
}
```

## B. .NET (ASP.NET Core) - Top 15

1. **Pipeline?** `Program.cs: UseRouting->UseAuthentication->UseAuthorization->MapControllers`. Order critical.
2. **DI lifetimes?** Singleton(stateless)/Scoped(per-request DbContext)/Transient(light). Captive dependency: don't inject Scoped into Singleton.
3. **Controllers + routing?** `[ApiController][Route("api/[controller]")]`, `[HttpGet("{id}")]`, `[FromBody]` DTO + `ModelState` validation.
4. **EF Core?** DbContext + DbSet, migrations `dotnet ef migrations add Init`, LINQ, `AsNoTracking()` for reads.
5. **Auth JWT?** `AddAuthentication(JwtBearer).AddJwtBearer(...)` + `[Authorize(Roles="Admin")]`. Validate issuer/audience/lifetime.
6. **Middleware custom?** `app.Use(async(ctx,next)=>{try{await next();}catch(ex){...}})` global exception handler.
7. **Config?** `IConfiguration`, `IOptions<T>`, user-secrets, env vars. Never hardcode connection string.
8. **Async?** `async Task<ActionResult<T>>` + `await ToListAsync()`. Avoid `.Result` deadlock.
9. **Validation?** DataAnnotations `[Required][StringLength]` + FluentValidation for complex.
10. **Status codes?** `Ok(), CreatedAtAction(), NoContent(), BadRequest(), Unauthorized(), Forbid(), NotFound()`.
11. **CORS?** `AddCors政策 AllowSpecificOrigins` + `UseCors()` before auth.
12. **Logging?** ILogger + Serilog sinks, correlation id.
13. **Testing?** xUnit + Moq + WebApplicationFactory for integration.
14. **Caching?** IMemoryCache / IDistributedCache Redis. `[ResponseCache]` for GET.
15. **Deploy?** `dotnet publish -c Release`, App Service / container, health checks `/health`.

## System Mini-Design (both tracks)
Prompt: Design URL shortener / todo API.
Say: Requirements -> API (POST /shorten, GET /:id) -> DB choice (Postgres for consistency, Mongo for flex) -> auth -> cache -> rate limit -> scale (stateless + LB).
