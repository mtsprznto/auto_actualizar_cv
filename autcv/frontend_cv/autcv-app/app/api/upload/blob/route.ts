import { NextResponse } from 'next/server';
import { put } from '@vercel/blob';

export async function POST(req: Request) {
  const formData = await req.formData();
  const file = formData.get('file') as File;

  if (!file) return NextResponse.json({ error: 'Archivo no enviado' }, { status: 400 });

  const { url } = await put(file.name, file, {
    access: 'public', // o 'private'
    allowOverwrite: true,
  });

  return NextResponse.json({ mensaje: 'Archivo subido correctamente', url });
}