"use client";

import { Button } from "@/components/ui/button";
import { CardHeader, CardTitle } from "@/components/ui/card";
import { Switch } from "@/components/ui/switch";
import { Textarea } from "@/components/ui/textarea";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip";
import { Loader2 } from "lucide-react";
import { useState } from "react";

interface SectionQuestionProps {
  questions: string;
  setQuestions: (value: string) => void;
  loading: boolean;
  response: string;
  generarRespuestas: () => void;
}

export function SectionQuestion({
  questions,
  setQuestions,
  loading,
  response,
  generarRespuestas,
}: SectionQuestionProps) {
  const [showInput, setShowInput] = useState(false);

  return (
    <>
      <CardHeader className="p-0">
        <div className="flex justify-between">
          <CardTitle>Ingrese una pregunta sobre la propuesta laboral</CardTitle>
          <Tooltip>
            <TooltipTrigger>
              <Switch
                checked={showInput}
                onCheckedChange={(value) => setShowInput(value)}
              />
            </TooltipTrigger>
            <TooltipContent>¿Preguntas?</TooltipContent>
          </Tooltip>
        </div>
      </CardHeader>
      {showInput && (
        <div className="space-y-2">
          <Textarea
            value={questions}
            onChange={(e) => setQuestions(e.target.value)}
            placeholder="¿Qué tipo de proyectos se esperan? ¿Cuál sería mi enfoque técnico?"
            disabled={loading}
            className="w-full h-[120px] resize-none"
            autoFocus
          />

          <div className="flex justify-end items-center">
            <Button
              onClick={generarRespuestas}
              disabled={loading || !questions.trim()}
              className="cursor-pointer bg-transparent text-white border hover:bg-white/3"
            >
              {loading ? (
                <Loader2 className="animate-spin w-4 h-4 mr-2 text-muted-foreground" />
              ) : (
                "Generar respuesta"
              )}
            </Button>
          </div>

          {response && (
            <Textarea
              value={response}
              placeholder="Respuesta generada"
              disabled={loading}
              className="w-full h-[150px] resize-none"
              autoFocus
            />
          )}
        </div>
      )}
    </>
  );
}
