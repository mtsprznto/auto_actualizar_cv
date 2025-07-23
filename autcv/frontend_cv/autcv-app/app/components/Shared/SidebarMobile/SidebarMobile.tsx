import { Menu } from "lucide-react";
import { Logo } from "../Logo";
import Link from "next/link";

export function SidebarMobile() {
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
