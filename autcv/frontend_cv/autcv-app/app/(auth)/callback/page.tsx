"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";

export default function AuthCallbackPage() {
  const router = useRouter();

  useEffect(() => {
    const handleAuthCallback = async () => {
      const { error } = await supabase.auth.getSession();
      if (error) {
        console.error("Error getting session:", error.message);
        router.push("/login?error=auth");
      } else {
        router.push("/"); // o redirige a dashboard
      }
    };

    handleAuthCallback();
  }, [router]);

  return (
    <div className="flex items-center justify-center h-screen">
      <p className="text-lg font-medium">Verificando tu cuenta...</p>
    </div>
  );
}
