"use client";

import { Button } from "@/components/ui/button";
import { CardHeader, CardTitle } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Download, Loader2 } from "lucide-react";
import Link from "next/link";

interface SectionProposalProps {
  propuesta: string;
  setPropuesta: (value: string) => void;
  loading: boolean;
  cvUrl?: string | null;
  generarCV: () => void;
}

export function SectionProposal({
  propuesta,
  setPropuesta,
  loading,
  cvUrl,
  generarCV,
}: SectionProposalProps) {
  return (
    <>
      <CardHeader className="p-0">
        <CardTitle>Ingrese la propuesta de trabajo</CardTitle>
      </CardHeader>
      <div className="space-y-2">
        <Textarea
          id="propuesta"
          rows={10}
          value={propuesta}
          onChange={(e) => setPropuesta(e.target.value)}
          placeholder="Escribí aquí la descripción de la propuesta..."
          disabled={loading}
          className="w-full h-[120px] resize-none "
          autoFocus
        />
        <div className="flex justify-end align-center">
          {loading ? (
            <Loader2 className="animate-spin w-4 h-4 mr-2" />
          ) : (
            <div className="flex gap-2">
              {cvUrl && (
                <Link href={cvUrl} target="_blank" rel="noopener noreferrer">
                  <Button className="cursor-pointer bg-transparent text-white border hover:bg-white/3">
                    <Download />
                  </Button>
                </Link>
              )}

              <Button
                onClick={generarCV}
                disabled={loading || !propuesta}
                className="cursor-pointer bg-transparent text-white border hover:bg-white/10"
              >
                Generar CV
              </Button>
            </div>
          )}
        </div>
      </div>
    </>
  );
}
