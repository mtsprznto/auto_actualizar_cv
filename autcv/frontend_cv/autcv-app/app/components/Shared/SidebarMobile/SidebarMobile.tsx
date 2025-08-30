"use client";
import { Menu } from "lucide-react";
import { Logo } from "../Logo";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import { useRouter } from "next/navigation";

import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { User } from "@supabase/supabase-js";

export function SidebarMobile() {
  const [user, setUser] = useState<User | null>(null);

  const router = useRouter();

  useEffect(() => {
    const checkSession = async () => {
      const {
        data: { session },
      } = await supabase.auth.getSession();

      const publicRoutes = ["/","/login", "/register", "/forgot-password"];
      const currentPath = window.location.pathname;

      if (!session?.user && !publicRoutes.includes(currentPath)) {
        router.push("/login");
      } else {
        setUser(session?.user ?? null);
      }
    };
    checkSession();
  }, [router]);


  const handleLogout = async () => {
    await supabase.auth.signOut();
    router.push("/login");
  };

  return (
    <nav className="bg-white/1 backdrop-blur-md border-b border-white/20 w-full">
      <div className="flex flex-row md:hidden p-3 justify-between mx-auto items-center">
        <Logo></Logo>
        <DropdownMenu>
          <DropdownMenuTrigger asChild>
            <button className="p-2 rounded-md border">
              <Menu />
            </button>
          </DropdownMenuTrigger>

          <DropdownMenuContent className=" h-screen w-screen rounded-none border-none">
            <DropdownMenuLabel>Mi cuenta</DropdownMenuLabel>
            <DropdownMenuSeparator />
            <DropdownMenuItem>Generar CV</DropdownMenuItem>
            {user ? (
              <>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={handleLogout}>
                  Cerrar sesión
                </DropdownMenuItem>
              </>
            ) : (
              <>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={() => router.push("/login")}>
                  Iniciar sesión
                </DropdownMenuItem>
                <DropdownMenuItem onClick={() => router.push("/register")}>
                  Registrarse
                </DropdownMenuItem>
              </>
            )}
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </nav>
  );
}
