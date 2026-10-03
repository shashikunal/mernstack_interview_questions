# 05 - Bonus: Next.js / NestJS / Azure-GCP

Interviewers give bonus points if you can compare, not deep-dive.

## Next.js (App Router) - Top 10
1. **SSR vs SSG vs ISR vs CSR?** SSR per-request (`dynamic`), SSG build-time, ISR revalidate, CSR client. Product page=ISR 60s, dashboard=CSR, checkout=SSR.
2. **App Router structure?** `app/page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `route.ts` API. `page` server by default.
3. **Server vs Client components?** Server: fetch DB directly, no hooks, smaller bundle. Client: `"use client"` for useState/useEffect/events. Default server.
4. **Data fetching?** `async function Page(){const d=await fetch(url,{next:{revalidate:60}})}` server. Client uses SWR/React Query.
5. **SEO?** `export const metadata={title,description}` + semantic + sitemap. Server renders meta.
6. **Route handlers?** `app/api/users/route.ts: export async function GET(){return Response.json(...)}`.
7. **Middleware?** `middleware.ts` for auth/redirect at edge before render.
8. **Image perf?** `<Image priority fill sizes>` auto optimize, lazy by default.
9. **Caching?** fetch cache + `revalidatePath('/')` / `revalidateTag('products')` after mutation.
10. **Deploy?** Vercel / Azure Static Web Apps / GCP Cloud Run container `next start`.

## NestJS - Top 10
1. **Building blocks?** Module->Controller->Service/Provider + DTO + Guard + Interceptor. `nest g resource users` scaffolds CRUD.
2. **DI?** `@Injectable()` + constructor inject. Singleton by default. Great for testing with mocks.
3. **Controller example?** `@Controller('users') @Get(':id') findOne(@Param('id') id:string){return this.svc.find(id)}`.
4. **Validation?** DTO class + `class-validator` + global `ValidationPipe({whitelist:true})`.
5. **Guard vs Interceptor vs Pipe?** Guard=allow? (auth), Pipe=transform/validate input, Interceptor=wrap req/res (logging/cache).
6. **Auth?** Passport JWT: `AuthGuard('jwt')` validates token, `@Req() req.user`. RolesGuard checks roles.
7. **Config + env?** `ConfigModule.forRoot({isGlobal:true})` + `config.get('DB_URL')`.
8. **DB?** TypeORM/Prisma module: `@InjectRepository(User) repo: Repository<User>`.
9. **Testing?** `Test.createTestingModule({providers:[Svc]})` + mock repo.
10. **Why Nest over Express?** Opinionated structure for teams, TS-first, scales to microservices. Express fine for small/fast.

## Azure / GCP - Top 10
1. **Where deploy MERN?** Azure: App Service + CosmosDB(Mongo API)/Postgres Flexible + Static Web Apps frontend. GCP: Cloud Run + Cloud SQL + Firebase Hosting.
2. **App Service vs Functions vs AKS?** App Service=simple API, Functions=event/serverless (webhook/cron), AKS=complex microservices.
3. **Env + secrets?** Azure Key Vault / GCP Secret Manager, never env in repo. Managed Identity / Workload Identity (no keys).
4. **CI/CD?** GitHub Actions -> `az webapp deploy` / `gcloud run deploy`. Stages: build->test->staging->prod + slot swap.
5. **Storage?** Blob/GCS for images + CDN (Front Door/Cloud CDN). Presigned URLs for upload.
6. **Monitoring?** App Insights / Cloud Trace + structured logs + alerts on 5xx/latency.
7. **Scaling?** Autoscale rules (CPU/RPS), stateless + LB, read replicas, Redis cache.
8. **Cost tip?** B1/App free tier dev, scale up prod, TTL logs, lifecycle cold storage.
9. **Docker deploy?** `Dockerfile multistage -> ACR/GAR -> Cloud Run/App Service container`.
10. **One-liner if no cloud exp?** "Deployed Node+React via Docker to Azure App Service with CI from GitHub, env via Key Vault, logs in App Insights. Eager to go deeper on GCP."

## Bonus One-Liners to Impress
- Next: "Used ISR 60s for catalog, server actions for mutations."
- Nest: "Guards for JWT+roles, interceptors for logging, pipes for DTO validation."
- Cloud: "Stateless containers + managed DB + CDN + autoscale."
