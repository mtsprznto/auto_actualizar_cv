"use client";
import Link from "next/link";
import { Logo } from "../Logo";
import { Button } from "@/components/ui/button";
import { CircleUser } from "lucide-react";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { SniperLoading } from "../Sniperloader";
import type { User } from "@supabase/supabase-js";

export function Navbar() {
  
const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchSession = async () => {
      const {
        data: { session },
        error,
      } = await supabase.auth.getSession();

      if (error) {
        console.error("Error fetching session:", error.message);
      } else if (session?.user) {
        setUser(session.user);
      }

      setLoading(false);
    };

    fetchSession();
  }, []);

  const handleLogout = async () => {
    await supabase.auth.signOut();
    location.reload();
  };

  if (loading) {
    return <SniperLoading />;
  }
  //console.log("USER: ", user);

  return (
    <nav className="bg-white/1 backdrop-blur-md border-b border-white/20">
      <div className="md:flex hidden p-3 justify-between max-w-[1000px] mx-auto items-center">
        <div className="">
          <Logo></Logo>
        </div>
        <div className="flex gap-3">
          <Link href="/generar-cv">
            <Button variant={"ghost"} className="border cursor-pointer">
              Generar Cv
            </Button>
          </Link>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" className="border cursor-pointer">
                <CircleUser />
              </Button>
            </DropdownMenuTrigger>

            <DropdownMenuContent className="flex flex-col w-56">
              <DropdownMenuLabel>Mi cuenta</DropdownMenuLabel>
              <DropdownMenuSeparator />

              {user ? (
                <>
                  <DropdownMenuItem asChild>
                    <Link href="/generar-cv">Generar CV</Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem asChild>
                    <Link href="/perfil">Perfil</Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem onClick={handleLogout}>
                    Cerrar sesión
                  </DropdownMenuItem>
                </>
              ) : (
                <>
                  <DropdownMenuItem asChild>
                    <Link href="/login">Iniciar sesión</Link>
                  </DropdownMenuItem>
                  <DropdownMenuItem asChild>
                    <Link href="/register">Registrarse</Link>
                  </DropdownMenuItem>
                </>
              )}
            </DropdownMenuContent>
          </DropdownMenu>
        </div>
      </div>
    </nav>
  );
}
