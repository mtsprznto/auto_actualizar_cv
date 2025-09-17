"use client";
import { Card, CardContent } from "@/components/ui/card";
import { Loader2 } from "lucide-react";
import { SectionProposal } from "./SectionProposal";
import { SectionQuestion } from "./SectionQuestion";

interface ViewGenerarCvProps {
  propuesta: string;
  setPropuesta: (propuesta: string) => void;
  cvUrl: string;
  loadingGenerar: boolean;
  loadingRespuestas: boolean;
  generarCV: () => void;

  questions: string;
  response: string;
  setQuestions: (questions: string) => void;
  generarRespuestas: () => void;
}

export function ViewGenerarCv({
  propuesta,
  setPropuesta,
  cvUrl,
  loadingGenerar,
  loadingRespuestas,
  generarCV,
  questions,
  response,
  setQuestions,
  generarRespuestas,
}: ViewGenerarCvProps) {
  return (
    <Card className="mx-auto md:mt-10 bg-[#1c031a] border-none">
      <div className="grid grid-cols-1 md:grid-cols-2">
        <CardContent className="space-y-4">
          <SectionProposal
            propuesta={propuesta}
            setPropuesta={setPropuesta}
            loading={loadingGenerar}
            cvUrl={cvUrl}
            generarCV={generarCV}
          />
          <SectionQuestion
            questions={questions}
            loading={loadingRespuestas}
            response={response}
            setQuestions={setQuestions}
            generarRespuestas={generarRespuestas}
          ></SectionQuestion>
        </CardContent>

        {/* CV GENERADO */}
        {loadingGenerar ? (
          <div className="flex justify-center items-center">
            <Loader2 className="animate-spin md:w-15 md:h-15 mr-2" />
          </div>
        ) : (
          <CardContent className="h-[500px] mb-6 py-4 md:py-0">
            <div className="h-full">
              {cvUrl ? (
                <object
                  key={cvUrl}
                  data={cvUrl}
                  type="application/pdf"
                  width="100%"
                  height="100%"
                  className="rounded"
                ></object>
              ) : (
                <>
                  <p className="text-center border w-full bg-[#f057ff] rounded-t text-[#1c031a]">
                    Preview del CV
                  </p>
                  <object
                    data={"/cv_placeholder/placeholder.pdf"}
                    type="application/pdf"
                    width="100%"
                    height="100%"
                    className="rounded"
                  ></object>
                </>
              )}
            </div>
          </CardContent>
        )}
      </div>
    </Card>
  );
}
