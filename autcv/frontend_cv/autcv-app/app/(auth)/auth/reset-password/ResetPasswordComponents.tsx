//app\(auth)\auth\reset-password\ResetPasswordComponents.tsx
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { supabase } from "@/lib/supabase";
import { cn } from "@/lib/utils";
import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

export default function ResetPasswordPage({
  className,
  ...props
}: React.ComponentProps<"div">) {
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [success, setSuccess] = useState<string | null>(null);
  const router = useRouter();

  const handleUpdatePassword = async (e: React.FormEvent) => {
    e.preventDefault();
    const { error } = await supabase.auth.updateUser({ password });

    if (error) {
      setError(error.message);
      setSuccess(null);
    } else {
      setError(null);
      setSuccess("Contraseña actualizada correctamente.");
      setTimeout(() => router.push("/login"), 3000);
    }
  };

  return (
    <div className={cn("flex flex-col gap-6 ", className)} {...props}>
      <Card className="mx-auto w-full">
        <CardHeader>
          <CardTitle>Actualizar contraseña</CardTitle>
          <CardDescription>
            Ingresa tu nueva contraseña para completar la restauración.
          </CardDescription>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleUpdatePassword} className="flex flex-col gap-6">
            <div className="grid gap-3">
              <Label htmlFor="password">Nueva contraseña</Label>
              <Input
                id="password"
                type="password"
                placeholder="••••••••"
                required
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <Button type="submit" className="w-full">
              Actualizar
            </Button>
            {error && <p className="text-sm text-red-500">{error}</p>}
            {success && <p className="text-sm text-green-600">{success}</p>}
            <div className="mt-4 text-center text-sm">
              ¿Ya tienes cuenta?{" "}
              <a href="/login" className="underline underline-offset-4">
                Login
              </a>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}
