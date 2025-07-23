"use client"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { useRouter } from "next/navigation";

interface ViewCardHomeProps {
  title: string;
  description?: string;
  content?: React.ReactNode;
  footer?: React.ReactNode;
  icon?: React.ReactNode;
  redirectTo?: string;
}

export function ViewCardHome({
  title,
  description,
  content,
  footer,
  icon,
  redirectTo,
}: ViewCardHomeProps) {
  const router = useRouter();

  return (
    <Card
      className="w-full bg-gradient-to-br from-purple-900/30 via-purple-700/20 to-purple-600/10 backdrop-blur-md border border-zinc-600/30 rounded-xl shadow-xl transition hover:scale-[1.02] hover:shadow-2xl duration-300 cursor-pointer"
      onClick={() => {
        if (redirectTo) {
          router.push(redirectTo);
        }
      }}
    >
      <CardHeader>
        <CardTitle className="flex align-center items-center gap-2">
          {icon && <span>{icon}</span>}
          <span>{title}</span>
        </CardTitle>
        {description && <CardDescription>{description}</CardDescription>}
      </CardHeader>
      {content && <CardContent>{content}</CardContent>}
      {footer && <CardFooter>{footer}</CardFooter>}
    </Card>
  );
}
