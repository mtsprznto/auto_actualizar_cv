// app\(auth)\forgot-password\page.tsx

import { ForgotPasswordForm } from "./ForgotPasswordForm";





export default async function Page() {
  

  return (
    <div className="flex  min-h-0 w-full items-center justify-center p-6 md:p-10 ">
      <div className="w-full max-w-sm">
        <ForgotPasswordForm />
      </div>
    </div>
  );
}
