// app/api/send-reset-email/route.ts
import { Resend } from "resend";
import { NextResponse } from "next/server";

const resend = new Resend(process.env.RESEND_API_KEY);

export async function POST(req: Request) {
  const { email } = await req.json();

  if (!email) {
    return NextResponse.json({ error: "Email requerido" }, { status: 400 });
  }

  await resend.emails.send({
    from: "tuapp@tudominio.com",
    to: email,
    subject: "Restauración de contraseña",
    html: `<p>Haz clic en el siguiente enlace para restaurar tu contraseña:</p>
           <a href="${process.env.NEXT_PUBLIC_BASE_URL}/auth/reset-password">Restaurar contraseña</a>`,
  });

  return NextResponse.json({ success: true });
}
