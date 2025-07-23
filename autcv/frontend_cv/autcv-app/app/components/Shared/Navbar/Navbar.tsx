"use client";
import Link from "next/link";
import { Logo } from "../Logo";
import { Button } from "@/components/ui/button";
import { User } from "lucide-react";

export function Navbar() {
  return (
    <nav className="bg-white/1 backdrop-blur-md border-b border-white/20">
      <div className="md:flex hidden p-3 justify-between max-w-[1000px] mx-auto items-center">
        <div className="">
          <Logo></Logo>
        </div>
        <div className="flex gap-4">
          <div>
            <Link href="/generar-cv">
              <Button variant={"ghost"} className="border cursor-pointer">Generar Cv</Button>
            </Link>
          </div>
          <div>
            <Link href="/">
              <Button variant={"ghost"}>
                <User></User>
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
