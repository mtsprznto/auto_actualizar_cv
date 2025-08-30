// app\(auth)\login\page.tsx
import { createServerComponentClient } from "@supabase/auth-helpers-nextjs";
import { LoginForm } from "./components/login-form";
import { cookies } from "next/headers";
import { redirect } from "next/navigation";

export default async function Page() {
  const supabase = createServerComponentClient({
    cookies,
  });

  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (user) {
    redirect("/"); // Redirige al home si ya hay sesión
  }


  return (
    <div className="flex  min-h-0 w-full items-center justify-center p-6 md:p-10 ">
      <div className="w-full max-w-sm">
        <LoginForm />
      </div>
    </div>
  );
}
