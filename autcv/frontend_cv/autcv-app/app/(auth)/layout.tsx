// app\(auth)\layout.tsx
import React from "react";
import { Navbar, SidebarMobile } from "../components/Shared";

// bg-gradient-to-b from-[#4e0058] to-[#a709c21]

export default function LayoutRoutes({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <main className="flex flex-col w-full">
      <div className="flex flex-row justify-between lg:hidden items-center">
        <div className="w-full flex-row">
          <SidebarMobile></SidebarMobile>
        </div>
      </div>
      <div className="flex">
        <div className="w-full h-screen relative ">
          <Navbar></Navbar>
          <div className="w-full md:max-w-[1500px] mx-auto h-[calc(100vh-58px)] md:h-[calc(100vh-94px)]">
            {children}
          </div>
        </div>
      </div>
    </main>
  );
}
