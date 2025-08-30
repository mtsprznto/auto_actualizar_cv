"use client";
import { Menu } from "lucide-react";
import { Logo } from "../Logo";
import Link from "next/link";
import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import { useRouter } from "next/navigation";

export function SidebarMobile() {
  const [user, setUser] = useState<any>(null);
  const [open, setOpen] = useState(false);
  const router = useRouter();

  useEffect(() => {
    const checkSession = async () => {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      if (!session?.user) {
        router.push("/login");
      } else {
        setUser(session.user);
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
        <Link href={"/"}>
          <Menu />
        </Link>
      </div>
    </nav>
  );
}
