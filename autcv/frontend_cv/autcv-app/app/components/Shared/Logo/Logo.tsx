import Link from "next/link";

export function Logo() {
  return (
    <Link href={"/"}>
      <div className="md:text-[30px] uppercase font-bold">
        <h1>Autcv</h1>
      </div>
    </Link>
  );
}
